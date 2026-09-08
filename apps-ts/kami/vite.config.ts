import babel from "@rolldown/plugin-babel";
import { tanstackRouter } from "@tanstack/router-plugin/vite";
import { vanillaExtractPlugin } from "@vanilla-extract/vite-plugin";
import react, { reactCompilerPreset } from "@vitejs/plugin-react";
import path from "node:path";
import { defineConfig, loadEnv } from "vite-plus";
import { fileURLToPath } from "node:url";
import tsconfigPaths from "vite-tsconfig-paths";

const configDir = path.dirname(fileURLToPath(import.meta.url));
const envDir = path.resolve(configDir, "../..");

// https://vite.dev/config/
export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, envDir);

  return {
    envDir: "../..",
    plugins: [
      // Please make sure that '@tanstack/router-plugin' is passed before '@vitejs/plugin-react'
      tanstackRouter({
        target: "react",
        autoCodeSplitting: true,
      }),
      react(),
      babel({ presets: [reactCompilerPreset()] }),
      tsconfigPaths(),
      vanillaExtractPlugin(),
    ],
    server: {
      port: mode != "prod" ? 5173 : Number(env.VITE_PROD_CLIENT_PORT),
    },
  };
});
