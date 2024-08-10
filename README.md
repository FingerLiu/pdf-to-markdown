# pdf-to-markdown
The simplest service to convert pdf to markdown with high quality(powered by gpt-4o and [gptpdf](https://github.com/CosmosShadow/gptpdf)).


This tool converts PDFs to Markdown format using GPT-4o, handling complex layouts like tables, links, equations, and multi-column content. It works particularly well with scanned PDFs and offers an easy way to extract editable text from complex documents.


## Features

- Converts PDFs to Markdown with support for tables, links, equations, and multi-column layouts.
- Handles scanned PDFs and complex document structures.
- Easy to set up and run locally.

## Quick Start

### 1. Install 


```bash
git clone git@github.com:FingerLiu/pdf-to-markdown.git
make install
```

### 2. Run
HINT: Because we use gpt-4o, you should set your openai key like shown in **env-example** before run.

```bash
make run
```

This will launch the FastAPI server with Uvicorn in development mode.


### 3. Have a try!

Access the application at `http://localhost:8000` and start converting your PDFs!

To use this tool, simply append the PDF link to the following URL as a parameter:

```
http://localhost:8000/?url=YOUR_PDF_LINK
```

For example:

```
http://localhost:8000/?url=https://arxiv.org/pdf/2408.00690
```

Replace `YOUR_PDF_LINK` with the URL of the PDF you wish to convert.



## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

