# drf-shop

# این سایت از Postgresql به عنوان پایگاه داده خود استفاده می کند
# قبل از اجرای آن مشخصات پایگاه داده خود را جایگزین کنید 
## Store/settings.py

DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql_psycopg2',
          'NAME': 'store',
          'USER': 'storedj',
          'PASSWORD': 'password',
          'HOST': 'localhost',
          'PORT': '',
      }
}
