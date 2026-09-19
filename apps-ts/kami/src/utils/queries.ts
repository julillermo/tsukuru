export async function validateQueryResponseBody(response: Response) {
  const body = await response.text();
  if (!response.ok) {
    throw new Error(`POST failed (${response.status}):\n ${body}`);
  }

  return body ? JSON.parse(body) : null;
}
