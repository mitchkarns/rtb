from apps.rtb.adsnative_rtb.process_rtb_v23 import RTBProcessorV23

for rtb_context in rtb_contexts:
    proc = RTBProcessorV23(rtb_context)
    campaigns = proc.convert_to_object()

for elem in campaigns:
    print elem
