import { StrictMode, React } from "react";
import { createRoot } from "react-dom/client";
import { App } from "./main";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <App />
  </StrictMode>
);
