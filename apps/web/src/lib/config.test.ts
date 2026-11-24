import { parseApiBaseUrl } from "./config";

describe("parseApiBaseUrl", () => {
  it("falls back to the local default when unset or blank", () => {
    expect(parseApiBaseUrl(undefined)).toBe("http://127.0.0.1:8000");
    expect(parseApiBaseUrl("   ")).toBe("http://127.0.0.1:8000");
  });

  it("strips a trailing slash", () => {
    expect(parseApiBaseUrl("https://api.example.test/")).toBe(
      "https://api.example.test",
    );
  });

  it("rejects malformed URLs", () => {
    expect(() => parseApiBaseUrl("not a url")).toThrow(/not a valid URL/);
  });

  it("rejects non-http protocols", () => {
    expect(() => parseApiBaseUrl("ftp://example.test")).toThrow(
      /http or https/,
    );
  });
});
