/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        accent: {
          50: "#eef4ff",
          100: "#dbe7ff",
          200: "#bcd2ff",
          300: "#8db3ff",
          400: "#5b8cf5",
          500: "#3a6fe0",
          600: "#2c57c2",
          700: "#26489d",
          800: "#233f7e",
          900: "#1f3666",
        },
      },
      fontFamily: {
        sans: [
          "Inter",
          "ui-sans-serif",
          "system-ui",
          "-apple-system",
          "Segoe UI",
          "sans-serif",
        ],
      },
      boxShadow: {
        card: "0 1px 2px rgba(15, 23, 42, 0.04), 0 4px 16px rgba(15, 23, 42, 0.06)",
        prompt:
          "0 1px 2px rgba(15, 23, 42, 0.04), 0 8px 28px rgba(58, 111, 224, 0.10)",
      },
    },
  },
  plugins: [],
};
