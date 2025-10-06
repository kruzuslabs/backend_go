package service

import (
	"log"

	gonanoid "github.com/matoous/go-nanoid/v2"
)

// defaultCharset contains the standard set of characters used for generating
// short IDs, including lowercase letters, uppercase letters, and digits.
const CHARLIST = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

// GenerateCode generates a random string of the given length using the provided
// charset. It wraps gonanoid.Generate and panics if generation fails, as
// failure is considered a programmer error.
//
// charset: the set of characters to use when generating the ID.
// length: the desired length of the generated string.
//
// Example usage:
//
//	> id := GenerateCode(defaultCharset, 8)
//	> fmt.Println(id)
//	> aZ3bY1kQ
func GenerateCode(charset string, length int) string {
	generatedID, err := gonanoid.Generate(charset, length)
	if err != nil {
		log.Fatalf("ID generation failed (len=%d): %v", length, err)
	}
	return generatedID
}
