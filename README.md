# Nyxt

Nyxt is a Python framework inspired by Next.js, designed to enable seamless navigation and dynamic components.

## Features
- No-reload page transitions
- Dynamic components
- State management

## Installation
1. Go to [releases](https://github.com/nyxt-app/Nyxt/releases) and select latest one
2. Click `Source Code (zip)` or `Source Code (tar.gz)` and it will begin download
3. Unzip the downloaded file in your project folder
4. Import nyxt into your main file:
```py
import nyxt
```

## Usage
```py
import nyxt
router = nyxt.Router()
app = nyxt.createApp("Nyxt")

app.Import(["TailwindCSS"])

navcomponent = nyxt.createComponent("navbar")
navcomponent.content("<h1>This is navbar</h1>")

children = nyxt.getChildren()

app.layout([
    navcomponent,
    children
])

router.style.default()

app.style.title("Nyxt - The Python Backend Framework")

nyxt.Start(host="0.0.0.0", port="3000")
```

## Requirements:
- Python 3.7+
- Flask

## License
This project is licensed under the MIT License.