from .create_app import getData as gAd
from .get_children import __init__ as gChild
from .create_component import getData as gCd
from .router import getData as gRt
from .importdat import *

import socket
import flask
import os
import re
import importlib.util
import random

def __init__(host, port, debug=None):
    class Color:
        RESET = "\033[0m"
        BLACK = "\033[30m"
        RED = "\033[31m"
        GREEN = "\033[32m"
        YELLOW = "\033[33m"
        BLUE = "\033[34m"
        MAGENTA = "\033[35m"
        CYAN = "\033[36m"
        WHITE = "\033[37m"
        BOLD = "\033[1m"
        UNDERLINE = "\033[4m"
        REVERSED = "\033[7m"
    
    def checkConnection(url):
        try:
            hostname = url.split("//")[-1].split("/")[0]
            socket.create_connection((hostname, 80), timeout=5)
            return True
        except OSError:
            return False
        
    
    def getBodyDataFromFile(path):
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL | re.IGNORECASE)
        return match.group(1).strip() if match else ""

    def createNyxtFolder():
        nyxt_path = os.path.join(os.getcwd(), ".nyxt")
        if os.path.exists(nyxt_path):
            return nyxt_path
        os.makedirs(nyxt_path)
        return nyxt_path

    def createFuncScript():
        random_name = "rqXeb22S9S.js"
        nyxt_path = createNyxtFolder()
        js_file_path = os.path.join(nyxt_path, random_name)
        with open(js_file_path, "w", encoding="utf-8") as js_file:
            js_file.write("""
document.addEventListener("DOMContentLoaded", () => {
    const variables = {
        aElement: true
    };

    function loadContent(url) {
        fetch(url)
            .then(response => response.text())
            .then(html => {
                const parser = new DOMParser();
                const doc = parser.parseFromString(html, "text/html");
                const newBodyElement = doc.getElementById("__nyxt-body");
                const bodyElement = document.getElementById("__nyxt-body");
                if (newBodyElement && bodyElement) {
                    while (bodyElement.firstChild) {
                        bodyElement.removeChild(bodyElement.firstChild);
                    }
                    bodyElement.innerHTML = newBodyElement.innerHTML;
                    bindAnchorEvents();
                } else {
                    window.location.href = url;
                }
            })
            .catch(error => window.location.href = url);
    }

    function bindAnchorEvents() {
        const bodyElement = document.getElementById("__nyxt-body");
        if (bodyElement) {
            let anchors = [
                ...bodyElement.querySelectorAll("a"),
                ...document.querySelectorAll("a[nyxt-link]")
            ];

            anchors.forEach(anchor => {
                let newAnchor = anchor.cloneNode(true);
                anchor.replaceWith(newAnchor);
            });

            anchors = [
                ...bodyElement.querySelectorAll("a"),
                ...document.querySelectorAll("a[nyxt-link]")
            ];

            anchors.forEach(anchor => {
                anchor.addEventListener("click", function(event) {
                    event.preventDefault();
                    const href = anchor.getAttribute("href");
                    const target = anchor.getAttribute("target");
                    if (href) {
                        const url = new URL(href, window.location.origin);
                        if (url.origin === window.location.origin) {
                            if (target === "_blank") {
                                window.open(url.href, "_blank");
                            } else {
                                history.replaceState({ path: url.href }, "", url.href);
                                loadContent(url.href);
                            }
                        } else {
                            window.location.href = url.href;
                        }
                    }
                });
            });
        } else {
            console.error("[NYXT]: Nyxt Body was not found!");
        }
    }

    if (variables.aElement) {
        console.log("[ ! ] This site is using Nyxt v1.0");
        bindAnchorEvents();
    }

    window.addEventListener("popstate", (event) => {
        if (event.state && event.state.path) {
            loadContent(event.state.path);
        }
    });
});
""")
        return f"<script src='/_nyxt/{random_name}' --nyxt-id='{random.randint(500, 185900)}{random.randint(100, 499)}' --nyxt-tag='imp-func-script'></script>"
    
    def processTitle():
        if gAd()["title"]:
            return gAd()["title"]
        else:
            return f"Nyxt App | {gAd()['name']}"

    def processGlobalStyle():
        style_file = "public/global.style.py"
        nyxt_dir = ".nyxt"
        css_file = os.path.join(nyxt_dir, "c-g-78d45DF4fd.css")
        script_file = os.path.join(nyxt_dir, "c-g-eeIKLDoldkfik.js")

        if not os.path.exists(style_file):
            print(f"{Color.GREEN}[NYXT]{Color.WHITE}: {Color.RED}Global styling file was not found, skipping process!{Color.WHITE}")
            return ""

        if not os.path.exists(nyxt_dir):
            os.makedirs(nyxt_dir)

        spec = importlib.util.spec_from_file_location("global_style", style_file)
        global_style = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(global_style)
        
        styles = global_style.style()
        css_output = ""
        script_output = ""

        for selector, properties in styles.items():
            css_output += f"{selector} {{\n"
            if "style" in properties:
                for rule in properties["style"]:
                    css_output += f"  {rule}\n"
            css_output += "}\n"

            if "classes" in properties and len(properties["classes"]) > 0:
                if not script_output:
                    script_output = "document.addEventListener(\"DOMContentLoaded\", function() {\n"
                script_output += f"    document.querySelectorAll(\"{selector}\").forEach(el => {{\n"
                script_output += "".join([f'        el.classList.add(\"{cls}\");\n' for cls in properties["classes"]])
                script_output += "    });\n"

        if script_output:
            script_output += "});\n"

        with open(css_file, "w", encoding="utf-8") as f:
            f.write(css_output)

        if script_output:
            with open(script_file, "w", encoding="utf-8") as f:
                f.write(script_output)

        return f"<link rel='stylesheet' href='/_nyxt/c-g-78d45DF4fd.css' --nyxt-id='{random.randint(500, 185900)}{random.randint(100, 499)}'>\n<script src='/_nyxt/c-g-eeIKLDoldkfik.js' --nyxt-id='{random.randint(500, 185900)}{random.randint(100, 499)}'></script>"

    def processImports():
        imports = ad["imports"]
        if imports:
            for imp in imports:
                if imp == "TailwindCSS":
                    if (checkConnection(tailwindCSS)):
                        return f'<script src="{tailwindCSS}" --nyxt-id="{random.randint(500, 758900)}{random.randint(100, 499)}"></script>'
                    else:
                        print(f"{Color.GREEN}[NYXT]{Color.WHITE}: {Color.RED}Couldnt connect to the server, please try again later and check your internet connection!{Color.WHITE}")
        return ""

    def loadLayout(childrenPath):
        layout = ad["lay"]
        temp_layout = ""

        for layoutComponent in layout:
            if layoutComponent == {"children": "dataManager", "childs": []}:
                temp_layout += f"<div id='__nyxt-body' style='height: 100vh;'>{getBodyDataFromFile(childrenPath)}</div>"
            else:
                temp_layout += str(layoutComponent)

        return f"""
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title --nyxt-id='{random.randint(500, 900)}{random.randint(100, 8767499)}'>{processTitle()}</title>
                    {processImports()}
                    {processGlobalStyle()}
                    {createFuncScript()}
                </head>
                <body>
                    {temp_layout}
                </body>
                </html>
    """
    
    def loadLayoutSTR(STR):
        layout = ad["lay"]
        temp_layout = ""

        for layoutComponent in layout:
            if layoutComponent == {"children": "dataManager", "childs": []}:
                temp_layout += f"<div id='__nyxt-body' style='height: 100vh;'>{str(STR)}</div>"
            else:
                temp_layout += str(layoutComponent)

        return f"""
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>{processTitle()}</title>
                    {processImports()}
                    {processGlobalStyle()}
                    {createFuncScript()}
                </head>
                <body>
                    {temp_layout}
                </body>
                </html>
    """

    data = {}
    ad = gAd()
    gc = gChild()
    cd = gCd()
    rt = gRt()

    app = flask.Flask(ad["name"])
    app.template_folder = "pages"

    createNyxtFolder()

    if ad["lay"]:
        if debug:
            print(f"{Color.GREEN}[NYXT]{Color.WHITE}: {Color.YELLOW}Layout initialization found...{Color.WHITE}")

    @app.route("/_nyxt/<path:filename>")
    def serve_nyxt_files(filename):
        return flask.send_from_directory(".nyxt", filename)
    
    @app.route("/public/<path:path>")
    def serve_public_files(path):
        return flask.send_from_directory("public", path)

    @app.route("/")
    def index():
        template_path = os.path.join(app.template_folder, "index.html")
        if not os.path.exists(template_path):
            return loadLayoutSTR("<div style='display: flex; justify-content: center; align-items: center; height: 100vh; background-color: #333; color: white; text-align: center;'><div><h1 style='font-size: 6rem; margin-bottom: 1rem;'>404</h1><p style='font-size: 1.5rem;'>This is default 404 page!</p></div></div>")

        return loadLayout(template_path)

    @app.route("/<path:path>")
    def myroute(path):
        if path == "favicon.ico":
            flask.abort(404)

        template_path = os.path.join(app.template_folder, f"{path}.html")
        if not os.path.exists(template_path):
            return loadLayoutSTR("<div style='display: flex; justify-content: center; align-items: center; height: 100vh; background-color: #333; color: white; text-align: center;'><div><h1 style='font-size: 6rem; margin-bottom: 1rem;'>404</h1><p style='font-size: 1.5rem;'>This is default 404 page!</p></div></div>")

        return loadLayout(template_path)

    app.run(host=host or "0.0.0.0", port=port or "25565", debug=debug or False)