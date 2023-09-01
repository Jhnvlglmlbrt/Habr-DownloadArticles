package doc

import (
	"fmt"
	path "habr-download-articles/path"
	"log"
	"os"
)

func SaveToTextFile(header, article string) {
	pathfile := path.GetFilePath()
	fmt.Println(pathfile)
	file, err := os.Create(pathfile)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	file.WriteString(header + "\n\n\n")
	file.WriteString(article)
}
