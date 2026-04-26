export default {
  async fetch(): Promise<Response> {
    return Response.json({
      ok: true,
      service: "org-platform-scheduler",
      note: "Use this Worker as a cron trigger that calls a private worker endpoint.",
    });
  },
};

