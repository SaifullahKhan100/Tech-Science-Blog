import django_filters
from articles.models import Article


class ArticleFilter(django_filters.FilterSet):
    CHOICES = (
        ('a', 'Ascending'),
        ('d', 'Descending')
    )

    ordering = django_filters.ChoiceFilter(label='Ordering', choices=CHOICES, method='myFilter')

    # class Meta:
    #     model = Article

    def myFilter(self, queryset, name, value):
        if value == 'a':
            exp = 'date'
        else:
            exp = '-date'
        print('value: ', value)
        return queryset.order_by(exp)
