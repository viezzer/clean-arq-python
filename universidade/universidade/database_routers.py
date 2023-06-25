class DatabaseRouter(object):

    def db_for_read(self, model, **hints):
        """Send all read operations on Example app models to `example_db`."""
        if str(model._meta) == 'app.alunosigiloso':
            return 'sensitive_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return True

    # def allow_migrate(self, db, app_label, model_name=None, **hints):
    #     """Ensure that the Example app's models get created on the right database."""
    #     if app_label == 'example':
    #         # The Example app should be migrated only on the example_db database.
    #         return db == 'example_db'
    #     elif db == 'example_db':
    #         # Ensure that all other apps don't get migrated on the example_db database.
    #         return False
    #
    #     # No opinion for all other scenarios
    #     return None