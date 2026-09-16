export const API_URL =
  import.meta.env.MODE === "self-host" ? "/self-host" : import.meta.env.VITE_API_URL;
