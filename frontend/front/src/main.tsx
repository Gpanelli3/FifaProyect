import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import App from "./App.tsx";

createRoot(document.getElementById("root")!).render(
  ////verifica el estado de los componentes
  <StrictMode>
    <App />
  </StrictMode>
);
