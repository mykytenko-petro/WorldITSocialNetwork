const parser = new DOMParser()

export function renderHTML(html) {
    return parser.parseFromString(html, "text/html").body.firstChild
}