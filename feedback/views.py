from django.shortcuts import render, redirect
from django.db.models.functions import ExtractYear
from .forms import ProductFeedbackForm
from .models import ProductFeedback

def product_feedback_view(request):
    if request.method == 'POST':
        form = ProductFeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_feedback')
    else:
        form = ProductFeedbackForm()

    feedback_list = ProductFeedback.objects.all().order_by('-created_at')

    # Unique years
    years_list = ProductFeedback.objects.annotate(year=ExtractYear('created_at')) \
                                    .values_list('year', flat=True) \
                                    .distinct()
    years_list = sorted(years_list, reverse=True)  # optional: latest year first

    # Months list
    months_list = [
        (1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'),
        (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'),
        (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')
    ]

    # Unique products
    product_list = feedback_list.values_list('product_name', flat=True).distinct()

    context = {
        'form': form,
        'feedback_list': feedback_list,
        'years_list': years_list,
        'months_list': months_list,
        'product_list': product_list,
    }
    return render(request, 'feedback/feedback.html', context)
