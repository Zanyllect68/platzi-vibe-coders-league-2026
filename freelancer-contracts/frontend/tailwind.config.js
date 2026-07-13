/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,jsx}'],
  theme: {
    extend: {
      colors: {
        background: 'oklch(0.988 0.006 95)',
        foreground: 'oklch(0.235 0.012 75)',
        card: 'oklch(0.997 0.003 95)',
        'card-foreground': 'oklch(0.235 0.012 75)',
        primary: {
          DEFAULT: 'oklch(0.42 0.072 168)',
          foreground: 'oklch(0.985 0.01 120)',
        },
        secondary: {
          DEFAULT: 'oklch(0.955 0.012 95)',
          foreground: 'oklch(0.3 0.015 75)',
        },
        muted: {
          DEFAULT: 'oklch(0.955 0.012 95)',
          foreground: 'oklch(0.52 0.014 80)',
        },
        accent: {
          DEFAULT: 'oklch(0.93 0.03 150)',
          foreground: 'oklch(0.32 0.05 168)',
        },
        destructive: {
          DEFAULT: 'oklch(0.55 0.2 27)',
          foreground: 'oklch(0.985 0.01 120)',
        },
        border: 'oklch(0.9 0.012 90)',
        input: 'oklch(0.9 0.012 90)',
        ring: 'oklch(0.42 0.072 168)',
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        display: ['Fraunces', 'Georgia', 'serif'],
      },
      borderRadius: {
        DEFAULT: '0.75rem',
      },
      boxShadow: {
        soft: '0 1px 2px oklch(0.3 0.02 80 / 0.04), 0 8px 24px -12px oklch(0.3 0.02 80 / 0.12)',
        card: '0 1px 3px oklch(0.3 0.02 80 / 0.05), 0 20px 50px -24px oklch(0.35 0.04 168 / 0.18)',
      },
    },
  },
  plugins: [],
}
