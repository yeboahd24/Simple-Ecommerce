from django.shortcuts import redirect, render
from product.models import Product
from .forms import ContactForm
from django.core.mail import send_mail


def frontpage(request):
    newest_products = Product.objects.all()[0:8]

    return render(request, 'core/frontpage.html', {'newest_products': newest_products})


def contact(request):
    send = False
    if request.method == 'POST':
        # Form was submitted
        form = ContactForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            subject = f"{cd['subject']}"
            message = f"{cd['message']}"
            email = f"{cd['email']}"

            send_mail(subject, message, email, ['yeboahd24@gmail.com'])
            sent = True
            return redirect('frontpage')

        else:
            form.add_error(None, "Ooh...Something went wrong, check form well")

    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
