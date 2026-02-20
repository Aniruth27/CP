import { merge } from "webpack-merge";
import MiniCssExtractPlugin from "mini-css-extract-plugin";
import common from "./webpack.common.js";
import path from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

export default merge(common, {
    mode: "development",
    devtool: "inline-source-map",

    module: {
        rules: [
            {
                test: /\.css$/i,
                use: [MiniCssExtractPlugin.loader, "css-loader"],
            },
        ],
    },

    plugins: [
        new MiniCssExtractPlugin({
            filename: "[name].css",
        }),
    ],

    devServer: {
        static: [
            {
                directory: path.join(__dirname, "dist"),
            },
            {
                directory: path.join(__dirname, "src/assets"),
                publicPath: "/assets",
            },
        ],
        port: 3000,
        open: true,
        hot: true,
        historyApiFallback: true,
    },
});
