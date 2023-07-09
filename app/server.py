import grpc
from helper.utils import retrive_answer
from concurrent import futures
import protos.questions_pb2 as q
import protos.questions_pb2_grpc as q_grpc

class QuestionAnswerService(q_grpc.QuestionAnswerServicer):
    def GetAnswer(self, request, context):
        # Here's where the hardcoded response comes in
        answer = retrive_answer(request.question)
        return q.AnswerResponse(answer=answer)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    q_grpc.add_QuestionAnswerServicer_to_server(QuestionAnswerService(), server)
    print('Starting server. Listening on port 50051.')
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()