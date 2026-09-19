import { API_URL } from "@/constants";
import { validateQueryResponseBody } from "@/utils/queries";
import { queryOptions } from "@tanstack/react-query";

// TODO: Eventually add zod for data validation
//    This means that I could also just use zod's infer instead of duplicating types
type getRandomConstructsQueryProps = {
  conceptNum: number;
  vocabNum: number;
};
export const getRandomConstructsQuery = (props: getRandomConstructsQueryProps) =>
  queryOptions({
    queryKey: ["randomConstructs"],
    enabled: false,
    queryFn: async () => {
      const response = await fetch(
        `${API_URL}/tsukuru/constructs/random?concepts=${props.conceptNum}&vocabs=${props.vocabNum}`,
        { method: "GET" },
      );
      return await validateQueryResponseBody(response);
    },
  });
