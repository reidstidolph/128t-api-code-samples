package main

import (
    "io/ioutil"
    "bytes"
    "net/http"
    "fmt"
    "crypto/tls"
)

func main() {
  url := "<Your_URL>"
  fmt.Println("URL:>", url)
  var bearer = "Bearer " + "<Your_Token>"

  var jsonStr = []byte(`{"<Your_Mod>": "<Your_Mod>"}`)
  req, _ := http.NewRequest("PATCH", url, bytes.NewBuffer(jsonStr))
  req.Header.Set("Content-Type", "application/json")
  req.Header.Add("Authorization", bearer)
  tr := &http.Transport{
          TLSClientConfig: &tls.Config{InsecureSkipVerify: true},
  }
  client := &http.Client{Transport: tr}
  resp, err := client.Do(req)
  if err != nil {
      panic(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)
    fmt.Println("response Body:", string(body))
}
