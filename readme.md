Book downloader
==============
This is a simple application using ghost.py to crawl pages with chapters on the page.

Usage
==============
Define variables in the main.py file:
`wrapping_div` A CSS3 selector for the div containing the chapter content.
`next_button` A CSS3 selector for the next button to click to get the next chapter.
`initial_url` The initial url for the browser to load and get content from
`series_name` Name of series to save in file

Run: 
* `make build` to construct the docker container.
* `make run` to download the chapters.

Downloaded chapters will appear in the chap folder.
