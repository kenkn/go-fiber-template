package routes

import (
	"$$$-api/controllers"
	"github.com/gofiber/fiber/v2"
)

func Setup(app *fiber.App) {
	app.Post("/hello", controllers.Hello)
}
