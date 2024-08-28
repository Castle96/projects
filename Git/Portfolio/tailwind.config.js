// tailwind.config.js
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/js/**/*.js",
  ],
  theme: {
    extend: {
      colors: {
        machiato: {
          base: "#f5e0dc",
          mantle: "#c6a0d6",
          crust: "#d6a89a",
          // Add more colors as needed
        },
        // Or include the whole palette
      },
    },
  },
  plugins: [],
}
