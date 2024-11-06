import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import Header from "./Header.jsx";
import App from './App.jsx'
import { TestComponent } from './TestComponent.jsx';

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <Header />
    <TestComponent />
  </StrictMode>,
)
