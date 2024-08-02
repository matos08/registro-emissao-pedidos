from fastapi import FastAPI
from fastapi_pagination import add_pagination


async def init_routers(app: FastAPI):
    from app.modules.core import health_check_router
    from app.modules.camiseta import routers as camiseta_router
    from app.modules.cliente import routers as cliente_router
    from app.modules.cor import routers as cor_router
    from app.modules.orcamento import routers as orcamento_router
    from app.modules.pedidos import routers as pedidos_router
    from app.modules.pintura import routers as pintura_router
    from app.modules.usuario import routers as usuario_router

    app.include_router(health_check_router.router)
    app.include_router(camiseta_router.router)
    app.include_router(cliente_router.router)
    app.include_router(cor_router.router)
    app.include_router(orcamento_router.router)
    app.include_router(pedidos_router.router)
    app.include_router(pintura_router.router)
    app.include_router(usuario_router.router)

    add_pagination(app)
