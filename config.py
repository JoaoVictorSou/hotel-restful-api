from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix='HOTELREST',
    settings_files= [
        'settings.toml',
        '.secrets.toml'
    ]
)