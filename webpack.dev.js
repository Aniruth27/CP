import { merge } from "webpack-merge";
import MiniCssExtractPlugin from "mini-css-extract-plugin";
import common from "./webpack.common.js";

export default merge(common, {
    mode: "development",
    devtool: "inline-source-map",

    module: {
        rules: [
            {
                test: /\.css$/i,
                use: [MiniCssExtractPlugin.loader, "css-loader", "postcss-loader"],
            },
        ],
    },

    plugins: [
        new MiniCssExtractPlugin({
            filename: "[name].css",
        }),
    ],

    devServer: {
        static: "./dist",
        port: 3000,
        open: true,
        hot: true,
        historyApiFallback: true,
    },
});
