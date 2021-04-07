from aiohttp import web


routes = web.RouteTableDef()


@routes.get("/")
async def handle(request):
    name = request.match_info.get("name", "Anonymous")
    text = f"Hello {name}"
    return web.Response(text=text)


app = web.Application()
app.add_routes(routes)

if __name__ == "__main__":
    web.run_app(app)
