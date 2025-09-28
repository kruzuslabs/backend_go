package api

import (
	"github.com/gin-gonic/gin"
)

// CreateShortURLHandler handles shortening a URL
func CreateShortURLHandler(c *gin.Context) {
	// parse request
	// call service to generate short code and store
	// return JSON response with short URL
	c.JSON(200, gin.H{
		"message": "Hello, world",
	})

}

// RedirectHandler handles redirection
func RedirectHandler(c *gin.Context) {
	// get code from path
	// check Redis, fallback to Postgres
	// increment analytics
	// redirect to original URL
	c.JSON(200, gin.H{
		"message": "Hello, world",
	})
}

// GetAnalyticsHandler returns click stats
func GetAnalyticsHandler(c *gin.Context) {
	// get code from path
	// fetch analytics from DB
	// return JSON response
	c.JSON(200, gin.H{
		"message": "Hello, world",
	})
}
