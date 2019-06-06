from django.urls import path

from . import views

# 複数のアプリケーションが存在するとき、url名の競合を防ぐために
# アプリケーションの名前空間を設定する
# templateではapp_name:nameで呼び出す
app_name = 'polls'
urlpatterns = [
    # nameの値はtemplateで{% url %}で呼ばれる
    # urlのパスを変更したいとき、template内での変更が不要になる
    # urls.pyのpath()で変更すれば良い
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]