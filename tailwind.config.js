/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    colors: {
      transparent: "transparent",
      bg: "#F8F8F8",
      gray: "#D9D9D9",
      darkgray: "#bfbfbf",
      black: "#36302D",
      title: "#C7404A",
      green: "#DAFFDB",
    },
    container: {
      center: true,
    },
    screens: {
      sm: "540px",
      md: "720px",
      lg: "960px",
      xl: "1140px",
      "2xl": "1320px",
    },
  },
  plugins: [],
};
