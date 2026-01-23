import path from 'path';
import { fileURLToPath } from 'url';
import HtmlWebpackPlugin from 'html-webpack-plugin';
import { globSync } from 'glob';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// AUTO-DETECT ALL HTML FILES IN THE ROOT (excluding node_modules)
const htmlFiles = globSync("./*.html");

// Generate HTML plugins automatically
const htmlPlugins = htmlFiles.map((file) => {
    return new HtmlWebpackPlugin({
        template: file,
        filename: path.basename(file), // output name (same as file name)
        chunks: ['main'], // Ensure it injects the main entry bundle
    });
});

export default {
    entry: {
        main: './src/main.js',
    },

    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: '[name].[contenthash].js',
        assetModuleFilename: 'assets/[name][ext]',
        clean: true,
    },

    module: {
        rules: [
            // HTML Loader
            {
                test: /\.html$/i,
                loader: "html-loader",
                options: {
                    sources: {
                        list: [
                            { tag: "img", attribute: "src", type: "src" },
                            { tag: "source", attribute: "srcset", type: "srcset" },
                        ],
                    },
                },
            },

            // Images
            {
                test: /\.(png|jpe?g|gif|svg)$/i,
                type: "asset/resource",
            },

            // Fonts
            {
                test: /\.(woff2?|ttf|eot|otf)$/i,
                type: "asset/resource",
            },
        ],
    },

    plugins: [
        ...htmlPlugins, // Auto detected pages
    ],
};
