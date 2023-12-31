/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["**/*.html", "**/*.py", "**/*.css"],
  theme: {
    extend: {
      colors: {
        bittersweet: {
          100: "#fcf8f8",
          200: "#ecc7c2",
          300: "#e7968c",
          400: "#ee6352",
          500: "#d64837",
          600: "#ac4336",
          700: "#874037",
          800: "#6a3b35",
          900: "#553531",
        },
        pictonblue: {
          100: "#fafbfc",
          200: "#cbdde5",
          300: "#9ec5d7",
          400: "#70b3d2",
          500: "#3fa7d6",
          600: "#388bb1",
          700: "#39718a",
          800: "#375c6d",
          900: "#334c57",
        },
        chocolatecosmos: {
          100: "#64383d",
          200: "#5b2b30",
          300: "#532026",
          400: "#490d14",
          500: "#45050c",
          600: "#350a0e",
          700: "#290c0f",
          800: "#200c0e",
          900: "#190c0d",
        },
        ivory: "#fffff0",
        atomictangerine: {
          200: "#f5cec3",
          300: "#f79d84",
          400: "#e2795c",
          500: "#ca5f42",
          600: "#a3543e",
          700: "#804b3c",
          800: "#664238",
          900: "#523a33"
        },
      }
    },
  },
  plugins: [],
}
