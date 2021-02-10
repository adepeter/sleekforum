class CacheDoesNotExistError(Exception):
    def __init__(self, message):
        self.message = message


class SiteSettingsNotConfigured(Exception):
    def __init__(self, message):
        self.message = message
