// BATTLEZONE: FIRESTORM — optional Go API starter.
// Run: go run services/go-api/main.go
package main

import (
	"encoding/json"
	"log"
	"net/http"
	"os"
	"time"
)

type Health struct {
	Status  string `json:"status"`
	Game    string `json:"game"`
	TimeUTC string `json:"time_utc"`
}

func main() {
	mux := http.NewServeMux()
	mux.HandleFunc("/health", func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json")
		_ = json.NewEncoder(w).Encode(Health{
			Status: "ok", Game: "BATTLEZONE: FIRESTORM",
			TimeUTC: time.Now().UTC().Format(time.RFC3339),
		})
	})
	addr := os.Getenv("ADDR")
	if addr == "" { addr = ":8080" }
	log.Printf("Game API listening on %s", addr)
	log.Fatal(http.ListenAndServe(addr, mux))
}
