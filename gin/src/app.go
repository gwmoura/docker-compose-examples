package main

import "github.com/gin-gonic/gin"

func main() {
	r := gin.Default()
	r.GET("/", func(c *gin.Context) {
		c.String(200, "I'am Online :D")
	})

	r.GET("/contact", func(c *gin.Context) {
		c.String(200, "I'am a contact ;)")
	})
	r.Run(":4000") // listen and serve on 0.0.0.0:8080
}
