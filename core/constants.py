from django.utils.translation import gettext_lazy as _


ACCOUNT_ACTIVATION_HOURS = 48

ACTIONS = {
    'add': {
        'title': _("add"),
        'level': 'primary',
        'icon': 'plus',
        'permission_prefix': 'add',
    },
    'add_images': {
        'title': _("add images"),
        'level': 'primary',
        'icon': 'plus',
        'permission_prefix': 'add',
    },
    'api_connect': {
        'title': _("connect"),
        'level': 'primary',
        'icon': 'link',
        'permission_prefix': 'change',
    },
    'backup_set.create_from_website': {
        'title': _("add backup"),
        'level': 'primary',
        'icon': 'plus',
        'permission_prefix': 'add',
    },
    'cancel': {
        'title': _("cancel"),
        'level': 'danger',
        'icon': 'stop',
        'permission_prefix': 'delete',
    },
    'capture': {
        'title': _("Capture"),
        'level': 'primary',
        'icon': 'screenshot',
        'permission_prefix': 'add'
    },
    'change': {
        'title': _("change"),
        'level': 'success',
        'icon': 'pencil',
        'permission_prefix': 'change',
    },
    'confirm_call_permission': {
        'title': _("confirm call permission"),
        'level': 'info',
        'icon': 'user',
        'permission_prefix': 'change'
    },
    'delete_image': {
        'title': _("delete all images"),
        'level': 'danger',
        'icon': 'trash',
        'permission_prefix': 'delete'
    },
    'delete_qanda': {
        'title': _("delete all q&a's"),
        'level': 'danger',
        'icon': 'trash',
        'permission_prefix': 'delete'
    },
    'export': {
        'title': _("Export"),
        'level': 'info',
        'icon': 'export',
        'permission_prefix': 'view',
    },
    'objects.confirm_call_permission': {
        'title': _("confirm call permission"),
        'level': 'info',
        'icon': 'user',
        'permission_prefix': 'change'
    },
    'objects.create_video': {
        'title': _("create video"),
        'level': 'primary',
        'icon': 'plus',
        'permission_prefix': 'add'
    },
    'objects.queue_video': {
        'title': _("queue video"),
        'level': 'primary',
        'icon': 'plus',
        'permission_prefix': 'add'
    },
    'objects.set_mapping': {
        'title': _("Mapping"),
        'level': 'info',
        'icon': 'upload',
        'permission_prefix': 'change'
    },
    'google_add': {
        'title': _("add from google"),
        'level': 'primary',
        'icon': 'plus',
        'permission_prefix': 'add',
    },
    'google_api_sync': {
        'title': _("Sync"),
        'level': 'info',
        'icon': 'refresh',
        'permission_prefix': 'change'
    },
    'delete': {
        'title': _("delete"),
        'level': 'danger',
        'icon': 'trash',
        'permission_prefix': 'delete',
    },
    'load': {
        'title': _("load"),
        'level': 'info',
        'icon': 'import',
        'permission_prefix': 'add'
    },
    'merge': {
        'title': _("merge"),
        'level': 'info',
        'icon': 'random',
        'permission_prefix': 'delete'
    },
    'objects.load': {
        'title': _("load"),
        'level': 'info',
        'icon': 'import',
        'permission_prefix': 'add'
    },
    'registrar_set.purchase': {
        'title': _("purchase"),
        'level': 'primary',
        'icon': 'plus',
        'permission_prefix': 'add'
    },
    'registrar_set.search': {
        'title': _("search"),
        'level': 'primary',
        'icon': 'search',
        'permission_prefix': 'view'
    },
    'api_sync': {
        'title': _("sync"),
        'level': 'info',
        'icon': 'refresh',
        'permission_prefix': 'add',
    },
    'permissions': {
        'title': _("permissions"),
        'level': 'info',
        'icon': 'wrench',
        'permission_prefix': 'change',
    },
    'send': {
        'title': _("send"),
        'level': 'info',
        'icon': 'envelope',
        'permission_prefix': 'send',
    },
    'search': {
        'title': _("search"),
        'level': 'info',
        'icon': 'search',
        'permission_prefix': 'add'
    },
    'refund': {
        'title': _("refund"),
        'level': 'warning',
        'icon': 'step-backward',
        'permission_prefix': 'refund',
    },
    'renew': {
        'title': _("Renew"),
        'level': 'info',
        'icon': 'refresh',
        'permission_prefix': 'change'
    },
    'gmb_set.remove_all': {
        'title': _("Remove all"),
        'level': 'danger',
        'icon': 'trash',
        'permission_prefix': 'delete'
    },
    'reset_login': {
        'title': _("Reset login"),
        'level': 'info',
        'icon': 'user',
        'permission_prefix': 'change'
    },
    'restore': {
        'title': _("Restore"),
        'level': 'info',
        'icon': 'cloud-upload',
        'permission_prefix': 'view'
    },
    'send_email_welcome': {
        'title': _("send welcome email"),
        'level': 'info',
        'icon': 'message',
        'permission_prefix': 'change'
    },
    'setup_dns_provider': {
        'title': _("setup dns provider"),
        'level': 'primary',
        'icon': 'wrench',
        'permission_prefix': 'change'
    },
    'setup_manager': {
        'title': _("setup manager"),
        'level': 'primary',
        'icon': 'wrench',
        'permission_prefix': 'change'
    },
    'subscribe': {
        'title': _("Subscribe"),
        'level': 'info',
        'icon': 'record',
        'permission_prefix': 'view'
    },
    'sync': {
        'title': _("sync"),
        'level': 'info',
        'icon': 'refresh',
        'permission_prefix': 'change'
    },
    'to_client': {
        'title': _("to client"),
        'level': 'info',
        'icon': 'user',
        'permission_prefix': 'add'
    },
    'to_lead': {
        'title': _("to lead"),
        'level': 'info',
        'icon': 'user',
        'permission_prefix': 'add'
    },
    'toggle_active': {
        'title': _("toggle active"),
        'level': 'info',
        'icon': 'check',
        'permission_prefix': 'change'
    },
    'uninstall_dns_provider': {
        'title': _("uninstall dns provider"),
        'level': 'danger',
        'icon': 'trash',
        'permission_prefix': 'change'
    },
    'upload': {
        'title': _("upload"),
        'level': 'primary',
        'icon': 'import',
        'permission_prefix': 'add'
    },
    'void': {
        'title': _("void"),
        'level': 'warning',
        'icon': 'step-backward',
        'permission_prefix': 'refund'
    },
    'reversilo': {
        'title': _("Do massive silo"),
        'level': 'info',
        'icon': 'plus',
        'permission_prefix': 'add'
    },
    'addwizard': {
    'title': _("Add Wizard"),
    'level': 'info',
    'icon': 'plus',
    'permission_prefix': 'add'
    },
    'sendfax': {
    'title': _("Send Fax"),
    'level': 'info',
    'icon': 'plus',
    'permission_prefix': 'add'
    },
    'fax_list': {
        'title': _("fax_list"),
        'level': 'info',
        'icon': 'trash',
        'permission_prefix': 'add',
    },
    'wfile': {
    'title': _("Get xlsx file"),
    'level': 'info',
    'icon': 'file',
    'permission_prefix': 'add'
    },
}

ALERT_COMMS_CALL = 'comms.call'
ALERT_PINGER_MONITORING = 'pinger.monitoring'

ALERT_CLASSES = (
    (ALERT_COMMS_CALL, _("COMMS - Call")),
    (ALERT_PINGER_MONITORING, _("Pinger - Monitoring")),
)

CICLE_DAY = 'day'
CICLE_WEEK = 'week'
CICLE_MONTH = 'month'
CICLE_YEAR = 'year'

COMMS_PLIVO = 'plivo'
COMMS_SIGNALWIRE = 'signalwire'
COMMS_TWILIO = 'twilio'
COMMS_SMSGATEWAY24 = 'smsgateway24'

COMPANY_NGINX = """
server {


    server_name www.%(domain)s %(domain)s;


    access_log /var/log/nginx/%(domain)s.access.log rt_cache;
    error_log /var/log/nginx/%(domain)s.error.log;

    root /var/www/%(domain)s/htdocs;

    location /.well-known/ {
        alias /var/www/%(domain)s/htdocs/.well-known/;
        access_log off;
    }

    location /.well-known/apple-app-site-association {
        alias /var/www/%(domain)s/htdocs/.well-known/apple-app-site-association;
        expires 1d;
        access_log off;
    }

    location / {
        proxy_pass http://backend;
        proxy_http_version 1.1;
        proxy_set_header Upgrade \$http_upgrade;
        proxy_set_header Connection "upgrade";

        proxy_redirect off;
        proxy_set_header Host \$http_host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
    }

    include /var/www/%(domain)s/conf/nginx/*.conf;
}
"""

DIRECTION_OUTBOUND = 'outbound'
DIRECTION_INBOUND = 'inbound'

EVENT_TASK = 'task'
EVENT_APPOINTMENT = 'appointment'
EVENT_CALL = 'call'
EVENT_JOB_START = 'job-start'
EVENT_PRIVATE = 'private'

EVENT_TASK_COLOR = '#641E16'
EVENT_APPOINTMENT_COLOR = '#512E5F'
EVENT_CALL_COLOR = '#154360'
EVENT_JOB_START_COLOR = '#0E6251'
EVENT_PRIVATE_COLOR = '#145A32'

GRACE_DAYS = 7

HREF_REGEX = r'href=(["\'])(.*?)\1'

LEVEL_ERROR = 'error'
LEVEL_INFO = 'info'
LEVEL_SUCCESS = 'success'
LEVEL_WARNING = 'warning'

MESSAGE_EMAIL = 'email'
MESSAGE_SMS = 'sms'

MODULE_CMS = 'cms'
MODULE_COMMS = 'comms'
MODULE_CONTRACTOR = 'contractor'
MODULE_CRM = 'crm'
MODULE_HOSTING = 'hosting'
MODULE_PINGER = 'pinger'
MODULE_SEO = 'seo'

MODULE_CMS_REQS = ()
MODULE_COMMS_REQS = ()
MODULE_CONTRACTOR_REQS = ('crm',)
MODULE_CRM_REQS = ()
MODULE_HOSTING_REQS = ()
MODULE_PINGER_REQS = ()
MODULE_SEO_REQS = ()

MODULE_LIST = (
    (MODULE_CMS, _("cms")),
    (MODULE_COMMS, _("comms")),
    (MODULE_CONTRACTOR, _("contractor")),
    (MODULE_CRM, _("crm")),
    (MODULE_HOSTING, _("hosting")),
    (MODULE_PINGER, _("pinger")),
    (MODULE_SEO, _("seo")),
)

MODULE_PRICE_LIST = (
    (MODULE_CMS, 19),
    (MODULE_CONTRACTOR, 19),
    (MODULE_COMMS, 19),
    (MODULE_CRM, 19),
    (MODULE_HOSTING, 19),
    (MODULE_PINGER, 19),
    (MODULE_SEO, 19),
)

MODULE_REQS_LIST = (
    (MODULE_CMS, MODULE_CMS_REQS),
    (MODULE_CONTRACTOR, MODULE_CONTRACTOR_REQS),
    (MODULE_COMMS, MODULE_COMMS_REQS),
    (MODULE_CRM, MODULE_CRM_REQS),
    (MODULE_HOSTING, MODULE_HOSTING_REQS),
    (MODULE_PINGER, MODULE_PINGER_REQS),
    (MODULE_SEO, MODULE_SEO_REQS),
)

NOTIFY_0 = 0
NOTIFY_10 = 10
NOTIFY_30 = 30
NOTIFY_60 = 60
NOTIFY_1440 = 24

PIXEL_GIF_DATA = """
R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7
""".strip()

RECURRING_CICLE = CICLE_MONTH
RECURRING_FEE = 50

URL_REGEX = (
    r'(\(.*?)?\b((?:https?|ftp|file):\/\/'
    r'[-a-z0-9+&@#\/%?=~_()|!:,.;]*[-a-z0-9+&@#\/%=~_()|])'
)
