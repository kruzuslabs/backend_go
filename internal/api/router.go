package api

import (
	"github.com/gin-gonic/gin"
)

// InitializeRoutes sets up all API endpoints
func InitializeRoutes(router *gin.Engine) {
	api := router.Group("/api/v1")
	{
		api.POST("/shorten", CreateShortURLHandler)
		api.GET("/:code", RedirectHandler)
		api.GET("/urls/:code", GetAnalyticsHandler)
	}
}
