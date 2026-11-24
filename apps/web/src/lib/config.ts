// Server-side configuration. The API base URL is not exposed to the browser.

const DEFAULT_API_BASE_URL = "http://127.0.0.1:8000";

export function parseApiBaseUrl(value: string | undefined): string {
  const raw = value?.trim() || DEFAULT_API_BASE_URL;
  let url: URL;
  try {
    url = new URL(raw);
  } catch {
    throw new Error(`API_BASE_URL is not a valid URL: "${raw}"`);
  }
  if (url.protocol !== "http:" && url.protocol !== "https:") {
    throw new Error(
      `API_BASE_URL must use http or https, got "${url.protocol}"`,
    );
  }
  return url.toString().replace(/\/$/, "");
}

export function getApiBaseUrl(): string {
  return parseApiBaseUrl(process.env.API_BASE_URL);
}
