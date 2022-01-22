package main

import (
	"log"

	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/fiber/v2/middleware/cors"
)

func main() {
	// port := os.Getenv("PORT")
	// GORMセット
	database.Connect()

	app := fiber.New()
	// CORSの設定
	app.Use(cors.New(cors.Config{
		AllowCredentials: true,
	}))

	routes.Setup(app)

	log.Fatal(app.Listen(":81"))
	// log.Fatal(app.Listen(":"+port))

}
