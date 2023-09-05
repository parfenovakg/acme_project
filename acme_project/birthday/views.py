# from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)
from django.urls import reverse_lazy
from .models import Birthday
from .forms import BirthdayForm
from .utils import calculate_birthday_countdown
# from django.core.paginator import Paginator


class BirthdayDetailView(DetailView):
    model = Birthday

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['birthday_countdown'] = calculate_birthday_countdown(
            self.object.birthday
        )
        return context 


class BirthdayMixin:
    model = Birthday
    success_url = reverse_lazy('birthday:list')


class BirthdayFormMixin:
    form_class = BirthdayForm
    template_name = 'birthday/birthday.html'


class BirthdayCreateView(BirthdayMixin, BirthdayFormMixin, CreateView):
    pass


class BirthdayUpdateView(BirthdayMixin, BirthdayFormMixin, UpdateView):
    pass


class BirthdayDeleteView(BirthdayMixin, DeleteView):
    pass


class BirthdayListView(ListView):
    # Указываем модель, с которой работает CBV...
    model = Birthday
    # ...сортировку, которая будет применена при выводе списка объектов:
    ordering = 'id'
    # ...и даже настройки пагинации:
    paginate_by = 10


# def delete_birthday(request, pk):
#     # Получаем объект модели или выбрасываем 404 ошибку.
#     instance = get_object_or_404(Birthday, pk=pk)
#     # В форму передаём только объект модели;
#     # передавать в форму параметры запроса не нужно.
#     form = BirthdayForm(instance=instance)
#     context = {'form': form}
#     # Если был получен POST-запрос...
#     if request.method == 'POST':
#         # ...удаляем объект:
#         instance.delete()
#         # ...и переадресовываем пользователя на страницу со списком записей.
#         return redirect('birthday:list')
#     # Если был получен GET-запрос — отображаем форму.
#     return render(request, 'birthday/birthday.html', context)


# # class BirthdayCreateView(CreateView):
# #     model = Birthday
# #     form_class = BirthdayForm
# #     template_name = 'birthday/birthday.html'
# #     success_url = reverse_lazy('birthday:list')


# # class BirthdayUpdateView(UpdateView):
# #     model = Birthday
# #     form_class = BirthdayForm
# #     template_name = 'birthday/birthday.html'
# #     success_url = reverse_lazy('birthday:list')


# # def birthday(request, pk=None):
# #     if pk is not None:
# #         instance = get_object_or_404(Birthday, pk=pk)
# #     else:
# #         instance = None
# #     form = BirthdayForm(
# #         request.POST or None,
# #         files=request.FILES or None,
# #         instance=instance)
# #     context = {'form': form}
# #     if form.is_valid():
# #         form.save()
# #         birthday_countdown = calculate_birthday_countdown(
# #             form.cleaned_data['birthday']
# #         )

# #         # Обновляем словарь контекста: добавляем в него новый элемент.
# #         context.update({'birthday_countdown': birthday_countdown})
# #         # age = calculate_age(form.cleaned_data['birthday'])
# #         # context.update({'age': age})
# #     return render(request, 'birthday/birthday.html', context)


# # class BirthdayListView(ListView):
#     # Указываем модель, с которой работает CBV...
#     model = Birthday
#     # ...сортировку, которая будет применена при выводе списка объектов:
#     ordering = 'id'
#     # ...и даже настройки пагинации:
#     paginate_by = 10


# def birthday_list(request):
#     # Получаем все объекты модели Birthday из БД.
#     birthdays = Birthday.objects.order_by('id')
#     # Передаём их в контекст шаблона.
#     paginator = Paginator(birthdays, 10)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {'page_obj': page_obj}
#     return render(request, 'birthday/birthday_list.html', context)
