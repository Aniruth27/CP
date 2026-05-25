import fs from 'fs';
import path from 'path';
import { globSync } from 'glob';

// Find all HTML files in src/
const htmlFiles = globSync('./src/*.html');

htmlFiles.forEach((file) => {
    // Keep download.html relative so Webpack still bundles all PDFs correctly
    if (path.basename(file) === 'download.html') {
        return;
    }

    let content = fs.readFileSync(file, 'utf8');
    let replaced = false;

    // Convert ./assets/[name].pdf or assets/[name].pdf to /assets/[name].pdf
    const regex = /href="(?:\.\/)?assets\/([^"]+\.pdf)"/g;
    
    if (regex.test(content)) {
        content = content.replace(regex, 'href="/assets/$1"');
        replaced = true;
    }

    if (replaced) {
        fs.writeFileSync(file, content, 'utf8');
        console.log(`Converted to absolute PDF link in: ${file}`);
    }
});

console.log('Absolute PDF link conversion completed successfully!');
