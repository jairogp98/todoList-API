from .users.routes import ns as users_ns
from .auth.routes import ns as auth_ns
from .tasks.routes import ns as tasks_ns

namespaces = [users_ns,auth_ns, tasks_ns]
