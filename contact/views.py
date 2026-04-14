from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage

def contact(request):
    if request.method == "POST":
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        #  Authenticated — pull from user object (tamper-proof)
        if request.user.is_authenticated:
            name = request.user.get_full_name() or request.user.first_name
            email = request.user.email
        else:
            #  Not authenticated — take from POST (they typed it manually)
            name = request.POST.get('name', '').strip()
            email = request.POST.get('email', '').strip()

        if not all([name, email, subject, message]):
            messages.error(request, "All fields are required.")
            return render(request, "contact.html", {
                'form_data': {'subject': subject, 'message': message},
                'user_name': name,
                'user_email': email,
            })

        #  Not logged in — save to session, redirect to login
        if not request.user.is_authenticated:
            request.session['pending_contact'] = {
                'name': name, 'email': email,
                'subject': subject, 'message': message
            }
            messages.warning(request, "Please login to send your message.")
            return redirect('/accounts/login/?next=/contact/')

        # ✅ Logged in — save to DB
        ContactMessage.objects.create(
            name=name, email=email,
            subject=subject, message=message
        )
        request.session.pop('pending_contact', None)
        messages.success(request, "Message sent successfully!")
        return redirect('contact')

    # ──────────────── GET ────────────────
    if request.user.is_authenticated:
        user_name = request.user.get_full_name() or request.user.first_name
        user_email = request.user.email
    else:
        user_name = ''
        user_email = ''

    pending = request.session.get('pending_contact')
    if request.user.is_authenticated and pending:
        return render(request, "contact.html", {
            'form_data': {
                'subject': pending.get('subject', ''),
                'message': pending.get('message', ''),
            },
            'user_name': user_name,
            'user_email': user_email,
        })

    return render(request, "contact.html", {
        'user_name': user_name,
        'user_email': user_email,
    })