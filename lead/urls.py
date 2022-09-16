from django.urls import path, include


from lead import views

urlpatterns = [
    path(
        'uploader/',
        views.LeadsUploader.as_view(),
        name='lead_uploader'
    ),
    path(
        'my-leads/',
        views.MyLeadsListView.as_view(),
        name='lead_my_list'
    ),
    path(
        'my-invoices/',
        views.MyInvoiceListView.as_view(),
        name='invoices_my_list'
    ),
    path(
        '<int:pk>/',
        include([
            path(
                '',
                views.BuyLeads.as_view(),
                name='lead_buy'
            ),
            path(
                'update/',
                views.LeadsUpdateView.as_view(),
                name='lead_update'
            ),
            path(
                'detail/',
                views.LeadsDetailView.as_view(),
                name='lead_detail'
            )
        ])
    ),
]
