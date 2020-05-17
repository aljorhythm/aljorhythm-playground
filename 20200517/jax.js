const mathjax = require("mathjax");
const { promises: fs } = require("fs");
const svg2imgCallback = require("svg2img");
const btoa = require('btoa')

svg2img = function (input, options = {}) {
    return new Promise((resolve, reject) => {
        svg2imgCallback(
            input,
            options,
            function (error, buffer) {
                if (error) return reject(error)
                resolve(buffer)
            });
    })
}
async function main() {
    const MathJax = await mathjax.init({
        loader: { load: ["input/tex", "output/svg"] }
    });
    async function svgHtmlToImage(svgHtml, filePath) {
        const outputBuffer = await svg2img('data:image/svg+xml;base64,' + btoa(svgHtml))
        await fs.writeFile(filePath, outputBuffer);
    }
    async function convertFile(filePath) {
        const tex = await fs.readFile(filePath, "utf-8");
        const svg = MathJax.tex2svg(tex, { display: true });
        const svgHtml = MathJax.startup.adaptor.innerHTML(svg);
        await fs.writeFile(`${filePath}.svg`, svgHtml)
        await svgHtmlToImage(svgHtml, `${filePath}.png`)
    }
    convertFile("first.tex");
}

main();
