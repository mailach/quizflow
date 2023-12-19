/**
 * plugins/vuetify.ts
 *
 * Framework documentation: https://vuetifyjs.com`
 */

// Styles
import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'

// Composables
import { createVuetify } from 'vuetify'

export default createVuetify({
  theme: {
    defaultTheme: 'dark', // Set the default theme to dark
    themes: {
      light: {
        colors: {
          primary: '#1867C0',
          secondary: '#5CBBF6',
          // ... other light theme colors
        },
      },
      dark: {
        dark: true, // This is important to denote this as a dark theme
        colors: {
          primary: '#9316a3',
          secondary: '#120f78',
          // ... other dark theme colors
          // You can define different color schemes for dark theme if you want
        },
      },
    },
  },
})
