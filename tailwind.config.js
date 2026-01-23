/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./about.html",
        "./contact.html",
        "./industry.html",
        "./product-details.html",
        "./products.html",
        "./download.html",
    ],
    theme: {
        extend: {
            colors: {
                primary: {
                    DEFAULT: '#248fce',
                    dark: '#1a7a9c',
                    light: '#e1f5fe',
                },
                secondary: {
                    DEFAULT: '#f3f4f6',
                }
            },
            fontFamily: {
                sans: ['Poppins', 'sans-serif'],
                poppins: ['Poppins', 'sans-serif'],
            },
        },
    },
    plugins: [],
}
